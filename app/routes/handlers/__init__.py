from app.routes.handlers.user_agent_handler import make_process_user_agent
from app.routes.handlers.echo_handler import make_process_echo
from app.routes.handlers.file_handler import make_file_handler
process_user_agent = make_process_user_agent()
process_echo = make_process_echo()
process_file_path = make_file_handler()

