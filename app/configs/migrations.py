from flask_migrate import Migrate

def init_app(app):
    from app.models.leads_model import Leads
    Migrate(app, app.db)

