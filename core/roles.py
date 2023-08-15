from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'can_create_blog_posts':True,
        'can_comment_on_blog_posts':True,
        'can_register_projects':True,
        'can_register_admin':True,
        'can_confirm_voluntary_participation':True,
        'can_register_expenses':True,
        'can_delete_reports':True,
    }


class Voluntary(AbstractUserRole):
    available_permissions = {
        'can_register_done_projects':True,
        'can_comment_on_blog_posts':True,
    
    }


class Supporter(AbstractUserRole):
    available_permissions = {
        'can_donate':True,
        'can_comment_on_blog_posts':True,
    }
