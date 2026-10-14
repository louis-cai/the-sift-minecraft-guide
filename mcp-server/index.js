/**
 * MCP Server for thesiftguide.com
 * Streamable HTTP protocol endpoint at /mcp
 */

const SERVER_INFO = {
  name: "com.thesiftguide/sift-tools",
  version: "1.0.0"
};

const TOOLS = [
  {
    name: "calculate_sift_portal_coordinates",
    description: "Convert coordinates between Minecraft Overworld, Nether, and The Sift (1:4 compression ratio). Matches thesiftguide.com algorithm.",
    inputSchema: {
      type: "object",
      properties: {
        x: { type: "number", description: "Origin X coordinate" },
        y: { type: "number", description: "Origin Y coordinate (defaults to 64)", default: 64 },
        z: { type: "number", description: "Origin Z coordinate" },
        direction: {
          type: "string",
          enum: ["overworld_to_sift", "sift_to_overworld", "nether_to_sift"],
          description: "Conversion direction",
          default: "overworld_to_sift"
        },
        ratio: { type: "number", description: "Compression ratio (standard Sift ratio is 4)", default: 4 }
      },
      required: ["x", "z"]
    }
  },
  {
    name: "calculate_sift_materials_budget",
    description: "Calculate portal frame block requirements and Echo Shard budget for The Sift gateway. Matches thesiftguide.com bill of materials.",
    inputSchema: {
      type: "object",
      properties: {
        frame_size: {
          type: "string",
          enum: ["standard", "compact", "arch"],
          description: "Portal frame size: standard (4x5), compact (3x3), or arch (7x9)",
          default: "standard"
        },
        include_corners: {
          type: "boolean",
          description: "Whether to include 4 corner blocks in frame construction",
          default: false
        }
      }
    }
  },
  {
    name: "diagnose_sift_ignition",
    description: "Diagnose Minecraft The Sift portal ignition issues and provide actionable next steps. Matches thesiftguide.com diagnostic rules.",
    inputSchema: {
      type: "object",
      properties: {
        setup_type: {
          type: "string",
          enum: ["vanilla", "modded"],
          description: "Minecraft installation type: vanilla or modded",
          default: "vanilla"
        },
        frame_block: {
          type: "string",
          enum: ["ancient", "custom"],
          description: "Frame block type: ancient (Reinforced Deepslate in Ancient City) or custom",
          default: "ancient"
        }
      }
    }
  }
];

function handleToolCall(name, args) {
  args = args || {};
  if (name === "calculate_sift_portal_coordinates") {
    const x = typeof args.x === 'number' ? args.x : 0;
    const y = typeof args.y === 'number' ? Math.round(args.y) : 64;
    const z = typeof args.z === 'number' ? args.z : 0;
    const dir = args.direction || "overworld_to_sift";
    const ratio = typeof args.ratio === 'number' && args.ratio > 0 ? args.ratio : 4;

    let targetX = 0;
    let targetY = y;
    let targetZ = 0;
    let modeDesc = "";

    if (dir === "overworld_to_sift") {
      targetX = Math.round(x / ratio);
      targetZ = Math.round(z / ratio);
      modeDesc = `Overworld to The Sift (1:${ratio} compression)`;
    } else if (dir === "sift_to_overworld") {
      targetX = Math.round(x * ratio);
      targetZ = Math.round(z * ratio);
      modeDesc = `The Sift to Overworld (${ratio}:1 expansion)`;
    } else if (dir === "nether_to_sift") {
      targetX = Math.round((x * 8) / ratio);
      targetZ = Math.round((z * 8) / ratio);
      modeDesc = `Nether to The Sift via Nether Bridge (${8 / ratio}x ratio)`;
    } else {
      targetX = Math.round(x / ratio);
      targetZ = Math.round(z / ratio);
      modeDesc = `Overworld to The Sift (1:${ratio} compression)`;
    }

    const distOrigin = Math.round(Math.sqrt(x * x + z * z));
    const distTarget = Math.round(Math.sqrt(targetX * targetX + targetZ * targetZ));
    const command = `/tp @s ${targetX} ${targetY} ${targetZ}`;

    const text = [
      `The Sift Portal Coordinate Calculation:`,
      `- Mode: ${modeDesc}`,
      `- Origin: X: ${x}, Y: ${y}, Z: ${z} (${distOrigin} blocks from origin)`,
      `- Destination: X: ${targetX}, Y: ${targetY}, Z: ${targetZ} (${distTarget} blocks from origin)`,
      `- Teleport Command: ${command}`,
      ``,
      `Source: thesiftguide.com`
    ].join("\n");

    return { content: [{ type: "text", text }] };
  }

  if (name === "calculate_sift_materials_budget") {
    const size = args.frame_size || "standard";
    const hasCorners = Boolean(args.include_corners);

    let frameBlocks = 0;
    let echoShards = 4;
    let outerDim = "";
    let innerDim = "";
    let desc = "";

    if (size === "compact") {
      outerDim = "3 × 3 blocks";
      innerDim = "1 × 1 (1 tile)";
      echoShards = 4;
      frameBlocks = 8;
      desc = hasCorners ? "Compact 3×3 square frame with full corner nodes." : "Compact 3×3 frame (8 blocks minimum).";
    } else if (size === "arch") {
      outerDim = "7 × 9 blocks";
      innerDim = "5 × 7 (35 tiles)";
      echoShards = 4;
      frameBlocks = hasCorners ? 28 : 20;
      desc = hasCorners ? "Colossal ancient rift gateway including 4 corner pylons." : "Ancient rift arch optimized without corners (20 blocks min).";
    } else {
      // standard
      outerDim = "4 × 5 blocks";
      innerDim = "2 × 3 (6 tiles)";
      echoShards = 4;
      frameBlocks = hasCorners ? 14 : 10;
      desc = hasCorners ? "Full 4×5 frame perimeter including 4 corner anchors." : "Cornerless 4×5 minimal frame (10 blocks minimum).";
    }

    const text = [
      `The Sift Portal Materials Budget:`,
      `- Frame Size: ${size.toUpperCase()} (${outerDim})`,
      `- Frame Opening: ${innerDim}`,
      `- Frame Blocks Required: ${frameBlocks} blocks (${hasCorners ? "with corners" : "cornerless"})`,
      `- Echo Shards Required: ${echoShards}x Echo Shards for activation`,
      `- Construction Note: ${desc}`,
      ``,
      `Source: thesiftguide.com`
    ].join("\n");

    return { content: [{ type: "text", text }] };
  }

  if (name === "diagnose_sift_ignition") {
    const setup = args.setup_type || "vanilla";
    let text = "";

    if (setup === "vanilla") {
      text = [
        `Portal Ignition Diagnostic: BLOCKED IN VANILLA SURVIVAL`,
        `- Status: Blocked`,
        `- Cause: The Reinforced Deepslate frame in Ancient Cities cannot be lit in pure vanilla survival without mods. Mojang has not enabled the dimension in vanilla 1.21. Clicking flint & steel will only spawn ordinary fire.`,
        `- Recommended Action: Install the official Sift dimension mod or fabric/forge datapac, or use the dev teleport command: /execute in sift:the_sift run tp @s ~ ~ ~`,
        ``,
        `Source: thesiftguide.com`
      ].join("\n");
    } else {
      text = [
        `Portal Ignition Diagnostic: READY TO ACTIVATE`,
        `- Status: Ready`,
        `- Cause: Modded environment detected. Standard fire does NOT light the portal.`,
        `- Required Steps:`,
        `  1. Ensure the 2x3 frame opening is clear of obstructing blocks.`,
        `  2. Hold an Echo Shard or craft a Soul Spark Igniter.`,
        `  3. Right-click the bottom center frame block.`,
        `  4. Step into the activated cyan void portal.`,
        ``,
        `Source: thesiftguide.com`
      ].join("\n");
    }

    return { content: [{ type: "text", text }] };
  }

  throw new Error(`Tool not found: ${name}`);
}

export default {
  async fetch(request) {
    const url = new URL(request.url);

    // CORS headers
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Accept, mcp-session-id"
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    // Health check or root GET
    if (request.method === "GET") {
      return new Response(JSON.stringify({
        status: "ok",
        server: SERVER_INFO.name,
        version: SERVER_INFO.version,
        tools: TOOLS.map(t => t.name),
        homepage: "https://thesiftguide.com"
      }, null, 2), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    if (request.method !== "POST") {
      return new Response("Method Not Allowed", { status: 405, headers: corsHeaders });
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return new Response(JSON.stringify({
        jsonrpc: "2.0",
        id: null,
        error: { code: -32700, message: "Parse error" }
      }), {
        status: 400,
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    const { id, method, params } = body;

    // Handle JSON-RPC methods
    if (method === "initialize") {
      return new Response(JSON.stringify({
        jsonrpc: "2.0",
        id,
        result: {
          protocolVersion: "2024-11-05",
          capabilities: {
            tools: { listChanged: false }
          },
          serverInfo: SERVER_INFO
        }
      }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    if (method === "notifications/initialized") {
      return new Response(JSON.stringify({ jsonrpc: "2.0", result: {} }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    if (method === "ping") {
      return new Response(JSON.stringify({ jsonrpc: "2.0", id, result: {} }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    if (method === "tools/list") {
      return new Response(JSON.stringify({
        jsonrpc: "2.0",
        id,
        result: { tools: TOOLS }
      }), {
        headers: { ...corsHeaders, "Content-Type": "application/json" }
      });
    }

    if (method === "tools/call") {
      try {
        const result = handleToolCall(params?.name, params?.arguments);
        return new Response(JSON.stringify({
          jsonrpc: "2.0",
          id,
          result
        }), {
          headers: { ...corsHeaders, "Content-Type": "application/json" }
        });
      } catch (err) {
        return new Response(JSON.stringify({
          jsonrpc: "2.0",
          id,
          error: { code: -32603, message: err.message }
        }), {
          status: 400,
          headers: { ...corsHeaders, "Content-Type": "application/json" }
        });
      }
    }

    return new Response(JSON.stringify({
      jsonrpc: "2.0",
      id,
      error: { code: -32601, message: `Method not found: ${method}` }
    }), {
      status: 404,
      headers: { ...corsHeaders, "Content-Type": "application/json" }
    });
  }
};
