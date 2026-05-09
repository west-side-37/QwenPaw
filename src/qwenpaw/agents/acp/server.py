app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Tells Northflank which port to use to stay online
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
)
from .server import QwenPawACPAgent, run_qwenpaw_agent
from .service import ACPService, get_acp_service, init_acp_service

__all__ = [
    "ACPAgentConfig",
    "ACPConfig",
    "ACPErrors",
    "ACPConfigurationError",
    "ACPProtocolError",
    "ACPSessionError",
    "ACPTransportError",
    "ACPService",
    "QwenPawACPAgent",
    "get_acp_service",
    "init_acp_service",
    "PermissionResolution",
    "run_qwenpaw_agent",
    "SuspendedPermission",
]
