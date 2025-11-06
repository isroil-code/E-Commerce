

def general_info(req):
    username = 'Guest'
    if req.user.is_authenticated:
        username = req.user.username
    return {
        'username':username,
    
    }