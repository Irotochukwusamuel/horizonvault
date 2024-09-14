# from sqlalchemy import JSON
#
# from application import db
# from application.Enums import Enums
# from application.Enums.Enums import NotificationClassesEnum
# from application.Mixins.GenericMixins import GenericMixin
# from exceptions.custom_exception import CustomException, ExceptionCode
#
#
# class Notification(db.Model, GenericMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     title = db.Column(db.String(350), nullable=True)
#     body = db.Column(db.String(350), nullable=True)
#     data = db.Column(JSON, default={})
#     status = db.Column(db.Enum(Enums.NotificationStatusEnum, nullable=True, values_callable=lambda x: [str(member.value) for member in Enums.NotificationStatusEnum]))
#     user = db.relationship("User", back_populates='notifications')
#
#     @staticmethod
#     def send_push_notification(user_id: str, title: str, body: str, notification_class: str, data: dict = None) -> bool:
#         """
#         Sends a push notification and stores the notification
#
#         Parameters:
#         user_id (str): The app user id of the user receiving the notification
#         title (str): The title of the notification
#         body (str): The body or content of the notification
#         notification_class (str): The type a notification is classified under, see NotificationClassesEnum for possible values
#         category (str): The category of the notification, see NotificationCategoryEnum for possible values
#         data (dict): A dictionary containing necessary data to pass on with the notification
#         """
#
#         if data is None:
#             data = {}
#
#         if not any(member.value == notification_class for member in NotificationClassesEnum):
#             raise CustomException(ExceptionCode.INVALID_NOTIFICATION)
#
#         user = User.query.filter_by(id=user_id).first()
#
#         if not user:
#             raise CustomException(ExceptionCode.ACCOUNT_NOT_FOUND)
#
#         push_notification_enabled = user.notification_settings[notification_class]['Push']
#
#         if push_notification_enabled:
#             # TODO: Implement SNS push notification
#             pass
#
#         notification = Notification(user_id=user.id, title=title, body=body, data=data, status=Enums.NotificationStatusEnum.UNREAD.value)  # noqa
#         db.session.add(notification)
#         db.session.commit()
#         db.session.refresh(notification)
#
#         return True
