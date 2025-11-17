class BaseView:
    def handle(self):
        return ["base"]

class AuthMixin(BaseView):
    def handle(self):
        return ["auth"] + super().handle()

class CacheMixin(BaseView):
    def handle(self):
        return ["cache"] + super().handle()

class ReportView(AuthMixin, CacheMixin):
    def handle(self):
        return ["report"] + super().handle()

print(ReportView().handle())


# Understand the Inheritance Structure
# BaseView
# ↑
# AuthMixin
# ↑
# ReportView

# and also

# BaseView
# ↑
# CacheMixin
# ↑
# ReportView

# So the inheritance is diamond-shaped:

#         BaseView
#        /        \
# AuthMixin     CacheMixin
#        \       /
#         ReportView

# Python Computes the MRO (Method Resolution Order)
ReportView.__mro__
#(ReportView, AuthMixin, CacheMixin, BaseView, object)
