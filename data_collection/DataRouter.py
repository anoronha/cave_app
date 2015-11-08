class GroundwaterRouter(object):
    """
    A router to control all database operations on models in the
    data_collection application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read data_collection models go to guam_groundwater.
        """
        if model._meta.app_label == 'data_collection':
            return 'guam_groundwater'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write data_collection models go to guam_groundwater.
        """
        if model._meta.app_label == 'data_collection':
            return 'guam_groundwater'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the data_collection app is involved.
        """
        if obj1._meta.app_label == 'data_collection' or \
           obj2._meta.app_label == 'data_collection':
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the data_collection app only appears in the 'guam_groundwater'
        database.
        """
        if app_label == 'data_collection':
            return db == 'guam_groundwater'
        return None
