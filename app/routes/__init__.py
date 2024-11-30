from app.routes.handlers import process_echo, process_user_agent, process_file_path

routes = {
    'echo': process_echo,
    'user-agent': process_user_agent,
    'files': process_file_path
}

