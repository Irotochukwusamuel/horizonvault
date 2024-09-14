from . import *


class NotificationModel:

    @classmethod
    def get_notifications(cls):
        _notifications = Notification.query.filter(Notification.user_id == current_user.id).order_by(Notification.created_at.desc()).all()
        notifications_data = [notification.to_dict(add_filter=False) for notification in _notifications]

        return {'notifications': notifications_data}

    @classmethod
    def mark_read(cls, notification_id):
        data: Notification = Notification.query.filter_by(id=int(notification_id)).first()

        if not data:
            raise CustomException(message="Notification not found", status_code=404)

        data.is_read = True
        db.session.commit()
        return "Notification has been marked read"

    @classmethod
    def delete_notification(cls, notification_id):
        data: Notification = Notification.query.filter_by(id=int(notification_id)).first()

        if not data:
            raise CustomException(message="Notification not found", status_code=404)

        data.delete()
        return "Notification has been deleted"
