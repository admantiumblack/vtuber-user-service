import os
import uvicorn
from Server.Config import get_server_settings

if __name__ == "__main__":
    run_setting = get_server_settings()
    uvicorn.run(
        "Server.startup:program", 
        host=run_setting.host, 
        port=run_setting.port, 
        reload=run_setting.reload
    )