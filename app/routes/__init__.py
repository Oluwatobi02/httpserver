from app.routes.handlers import process_echo, process_user_agent

routes = {
    'echo': process_echo,
    'user-agent': process_user_agent
}

