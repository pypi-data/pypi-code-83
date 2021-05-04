# -*- coding: utf-8 -*-
from notifiqueme import modulo
obj = modulo.Notification("66dd4a3c-d13d-40ba-a363-df10139fe15c", str("dK0OwqepDaQAib9EyqXveFstdhdUtICEhmrKx-UW"))
p = obj.Send(5531989715963, "11- credenciais da conta do michael", modulo.NotificationType.WHATSAPP)
print(p)