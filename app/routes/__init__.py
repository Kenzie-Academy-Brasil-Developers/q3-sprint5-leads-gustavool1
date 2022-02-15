from app.routes.leads_route import bp as bp_leads

def init_app(app):
    app.register_blueprint(bp_leads)