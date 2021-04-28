# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['GameServerDeploymentRolloutArgs', 'GameServerDeploymentRollout']

@pulumi.input_type
class GameServerDeploymentRolloutArgs:
    def __init__(__self__, *,
                 default_game_server_config: pulumi.Input[str],
                 deployment_id: pulumi.Input[str],
                 game_server_config_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GameServerDeploymentRollout resource.
        :param pulumi.Input[str] default_game_server_config: This field points to the game server config that is
               applied by default to all realms and clusters. For example,
               `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        :param pulumi.Input[str] deployment_id: The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        :param pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]] game_server_config_overrides: The game_server_config_overrides contains the per game server config
               overrides. The overrides are processed in the order they are listed. As
               soon as a match is found for a cluster, the rest of the list is not
               processed.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "default_game_server_config", default_game_server_config)
        pulumi.set(__self__, "deployment_id", deployment_id)
        if game_server_config_overrides is not None:
            pulumi.set(__self__, "game_server_config_overrides", game_server_config_overrides)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="defaultGameServerConfig")
    def default_game_server_config(self) -> pulumi.Input[str]:
        """
        This field points to the game server config that is
        applied by default to all realms and clusters. For example,
        `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        """
        return pulumi.get(self, "default_game_server_config")

    @default_game_server_config.setter
    def default_game_server_config(self, value: pulumi.Input[str]):
        pulumi.set(self, "default_game_server_config", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Input[str]:
        """
        The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="gameServerConfigOverrides")
    def game_server_config_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]:
        """
        The game_server_config_overrides contains the per game server config
        overrides. The overrides are processed in the order they are listed. As
        soon as a match is found for a cluster, the rest of the list is not
        processed.
        Structure is documented below.
        """
        return pulumi.get(self, "game_server_config_overrides")

    @game_server_config_overrides.setter
    def game_server_config_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]):
        pulumi.set(self, "game_server_config_overrides", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _GameServerDeploymentRolloutState:
    def __init__(__self__, *,
                 default_game_server_config: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 game_server_config_overrides: Optional[pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GameServerDeploymentRollout resources.
        :param pulumi.Input[str] default_game_server_config: This field points to the game server config that is
               applied by default to all realms and clusters. For example,
               `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        :param pulumi.Input[str] deployment_id: The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        :param pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]] game_server_config_overrides: The game_server_config_overrides contains the per game server config
               overrides. The overrides are processed in the order they are listed. As
               soon as a match is found for a cluster, the rest of the list is not
               processed.
               Structure is documented below.
        :param pulumi.Input[str] name: The resource id of the game server deployment eg:
               'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if default_game_server_config is not None:
            pulumi.set(__self__, "default_game_server_config", default_game_server_config)
        if deployment_id is not None:
            pulumi.set(__self__, "deployment_id", deployment_id)
        if game_server_config_overrides is not None:
            pulumi.set(__self__, "game_server_config_overrides", game_server_config_overrides)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="defaultGameServerConfig")
    def default_game_server_config(self) -> Optional[pulumi.Input[str]]:
        """
        This field points to the game server config that is
        applied by default to all realms and clusters. For example,
        `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        """
        return pulumi.get(self, "default_game_server_config")

    @default_game_server_config.setter
    def default_game_server_config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_game_server_config", value)

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        """
        return pulumi.get(self, "deployment_id")

    @deployment_id.setter
    def deployment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_id", value)

    @property
    @pulumi.getter(name="gameServerConfigOverrides")
    def game_server_config_overrides(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]:
        """
        The game_server_config_overrides contains the per game server config
        overrides. The overrides are processed in the order they are listed. As
        soon as a match is found for a cluster, the rest of the list is not
        processed.
        Structure is documented below.
        """
        return pulumi.get(self, "game_server_config_overrides")

    @game_server_config_overrides.setter
    def game_server_config_overrides(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]):
        pulumi.set(self, "game_server_config_overrides", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the game server deployment eg:
        'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class GameServerDeploymentRollout(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_game_server_config: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 game_server_config_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This represents the rollout state. This is part of the game server
        deployment.

        To get more information about GameServerDeploymentRollout, see:

        * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/GameServerDeploymentRollout)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/game-servers/docs)

        ## Example Usage
        ### Game Service Deployment Rollout Basic

        ```python
        import pulumi
        import json
        import pulumi_gcp as gcp

        default_game_server_deployment = gcp.gameservices.GameServerDeployment("defaultGameServerDeployment",
            deployment_id="tf-test-deployment",
            description="a deployment description")
        default_game_server_config = gcp.gameservices.GameServerConfig("defaultGameServerConfig",
            config_id="tf-test-config",
            deployment_id=default_game_server_deployment.deployment_id,
            description="a config description",
            fleet_configs=[gcp.gameservices.GameServerConfigFleetConfigArgs(
                name="some-non-guid",
                fleet_spec=json.dumps({
                    "replicas": 1,
                    "scheduling": "Packed",
                    "template": {
                        "metadata": {
                            "name": "tf-test-game-server-template",
                        },
                        "spec": {
                            "ports": [{
                                "name": "default",
                                "portPolicy": "Dynamic",
                                "containerPort": 7654,
                                "protocol": "UDP",
                            }],
                            "template": {
                                "spec": {
                                    "containers": [{
                                        "name": "simple-udp-server",
                                        "image": "gcr.io/agones-images/udp-server:0.14",
                                    }],
                                },
                            },
                        },
                    },
                }),
            )])
        default_game_server_deployment_rollout = gcp.gameservices.GameServerDeploymentRollout("defaultGameServerDeploymentRollout",
            deployment_id=default_game_server_deployment.deployment_id,
            default_game_server_config=default_game_server_config.name)
        ```

        ## Import

        GameServerDeploymentRollout can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout default projects/{{project}}/locations/global/gameServerDeployments/{{deployment_id}}/rollout
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout default {{project}}/{{deployment_id}}
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout default {{deployment_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_game_server_config: This field points to the game server config that is
               applied by default to all realms and clusters. For example,
               `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        :param pulumi.Input[str] deployment_id: The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]] game_server_config_overrides: The game_server_config_overrides contains the per game server config
               overrides. The overrides are processed in the order they are listed. As
               soon as a match is found for a cluster, the rest of the list is not
               processed.
               Structure is documented below.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GameServerDeploymentRolloutArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This represents the rollout state. This is part of the game server
        deployment.

        To get more information about GameServerDeploymentRollout, see:

        * [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/GameServerDeploymentRollout)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/game-servers/docs)

        ## Example Usage
        ### Game Service Deployment Rollout Basic

        ```python
        import pulumi
        import json
        import pulumi_gcp as gcp

        default_game_server_deployment = gcp.gameservices.GameServerDeployment("defaultGameServerDeployment",
            deployment_id="tf-test-deployment",
            description="a deployment description")
        default_game_server_config = gcp.gameservices.GameServerConfig("defaultGameServerConfig",
            config_id="tf-test-config",
            deployment_id=default_game_server_deployment.deployment_id,
            description="a config description",
            fleet_configs=[gcp.gameservices.GameServerConfigFleetConfigArgs(
                name="some-non-guid",
                fleet_spec=json.dumps({
                    "replicas": 1,
                    "scheduling": "Packed",
                    "template": {
                        "metadata": {
                            "name": "tf-test-game-server-template",
                        },
                        "spec": {
                            "ports": [{
                                "name": "default",
                                "portPolicy": "Dynamic",
                                "containerPort": 7654,
                                "protocol": "UDP",
                            }],
                            "template": {
                                "spec": {
                                    "containers": [{
                                        "name": "simple-udp-server",
                                        "image": "gcr.io/agones-images/udp-server:0.14",
                                    }],
                                },
                            },
                        },
                    },
                }),
            )])
        default_game_server_deployment_rollout = gcp.gameservices.GameServerDeploymentRollout("defaultGameServerDeploymentRollout",
            deployment_id=default_game_server_deployment.deployment_id,
            default_game_server_config=default_game_server_config.name)
        ```

        ## Import

        GameServerDeploymentRollout can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout default projects/{{project}}/locations/global/gameServerDeployments/{{deployment_id}}/rollout
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout default {{project}}/{{deployment_id}}
        ```

        ```sh
         $ pulumi import gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout default {{deployment_id}}
        ```

        :param str resource_name: The name of the resource.
        :param GameServerDeploymentRolloutArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GameServerDeploymentRolloutArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_game_server_config: Optional[pulumi.Input[str]] = None,
                 deployment_id: Optional[pulumi.Input[str]] = None,
                 game_server_config_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GameServerDeploymentRolloutArgs.__new__(GameServerDeploymentRolloutArgs)

            if default_game_server_config is None and not opts.urn:
                raise TypeError("Missing required property 'default_game_server_config'")
            __props__.__dict__["default_game_server_config"] = default_game_server_config
            if deployment_id is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_id'")
            __props__.__dict__["deployment_id"] = deployment_id
            __props__.__dict__["game_server_config_overrides"] = game_server_config_overrides
            __props__.__dict__["project"] = project
            __props__.__dict__["name"] = None
        super(GameServerDeploymentRollout, __self__).__init__(
            'gcp:gameservices/gameServerDeploymentRollout:GameServerDeploymentRollout',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_game_server_config: Optional[pulumi.Input[str]] = None,
            deployment_id: Optional[pulumi.Input[str]] = None,
            game_server_config_overrides: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'GameServerDeploymentRollout':
        """
        Get an existing GameServerDeploymentRollout resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_game_server_config: This field points to the game server config that is
               applied by default to all realms and clusters. For example,
               `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        :param pulumi.Input[str] deployment_id: The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameServerDeploymentRolloutGameServerConfigOverrideArgs']]]] game_server_config_overrides: The game_server_config_overrides contains the per game server config
               overrides. The overrides are processed in the order they are listed. As
               soon as a match is found for a cluster, the rest of the list is not
               processed.
               Structure is documented below.
        :param pulumi.Input[str] name: The resource id of the game server deployment eg:
               'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GameServerDeploymentRolloutState.__new__(_GameServerDeploymentRolloutState)

        __props__.__dict__["default_game_server_config"] = default_game_server_config
        __props__.__dict__["deployment_id"] = deployment_id
        __props__.__dict__["game_server_config_overrides"] = game_server_config_overrides
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return GameServerDeploymentRollout(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultGameServerConfig")
    def default_game_server_config(self) -> pulumi.Output[str]:
        """
        This field points to the game server config that is
        applied by default to all realms and clusters. For example,
        `projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config`.
        """
        return pulumi.get(self, "default_game_server_config")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="gameServerConfigOverrides")
    def game_server_config_overrides(self) -> pulumi.Output[Optional[Sequence['outputs.GameServerDeploymentRolloutGameServerConfigOverride']]]:
        """
        The game_server_config_overrides contains the per game server config
        overrides. The overrides are processed in the order they are listed. As
        soon as a match is found for a cluster, the rest of the list is not
        processed.
        Structure is documented below.
        """
        return pulumi.get(self, "game_server_config_overrides")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource id of the game server deployment eg:
        'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

