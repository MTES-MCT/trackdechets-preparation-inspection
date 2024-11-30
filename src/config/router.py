class DbRouter:
    wh_db = "spatial"
    default_db = "default"

    def db_for_read(self, model, **hints):
        if model._meta.app_label == "maps":
            return self.wh_db
        else:
            return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "maps":
            raise Exception("This model is read only!")

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "maps":
            return False

        return db == "default"
