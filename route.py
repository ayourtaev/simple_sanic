from resource import simple_resource

routes = [simple_resource.EchoResource.as_view(), '/echo_subscription', ['POST']]
