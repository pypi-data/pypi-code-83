from bergen.messages.postman.progress import ProgressLevel
from bergen.debugging import DebugLevel
from bergen.handlers.base import ContractHandler
from bergen.messages import BouncedForwardedAssignMessage, AssignYieldsMessage, AssignProgressMessage, AssignDoneMessage, AssignReturnMessage, AssignCriticalMessage
from bergen.console import console


class AssignHandler(ContractHandler[BouncedForwardedAssignMessage]):

    @property
    def meta(self):
        return {"extensions": self.message.meta.extensions, "reference": self.message.meta.reference}

    async def log(self, message, level =ProgressLevel.INFO):
        console.log(message)
        await self.pass_progress(message, level=level)

    async def pass_yield(self, value):
        yield_message = AssignYieldsMessage(data={"returns": value}, meta=self.meta)
        await self.forward(yield_message)

    async def pass_progress(self, value, level: ProgressLevel = ProgressLevel.INFO):
        progress_message = AssignProgressMessage(data={"message": value, "level": level.value}, meta=self.meta)
        await self.forward(progress_message)

    async def pass_done(self):
        return_message = AssignDoneMessage(data={"ok": True}, meta=self.meta)
        await self.forward(return_message)

    async def pass_result(self, value):
        return_message = AssignReturnMessage(data={"returns": value}, meta=self.meta)
        await self.forward(return_message)

    async def pass_exception(self, exception):
        error_message = AssignCriticalMessage(data={"message": str(exception), "type": str(exception.__class__.__name__)}, meta=self.meta)
        await self.forward(error_message)