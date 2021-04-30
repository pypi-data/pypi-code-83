import argparse

import boto3
import jmespath

DEFAULT_REGION = "eu-west-1"
NAME = "name"
IP = "ip"

PATTERN_KAFKA_BROKER = "-confluent-broker-"
PATTERN_KAFKA_WORKER = "-confluent-worker-"

KAFKA_BOOTSTRAP_PORT = 9092


def __get_ec2_ips_and_names(region):
    client = boto3.client("ec2", region_name=region)
    response = client.describe_instances(
        Filters=[
            {
                "Name": "tag-key",
                "Values": [
                    "Name",
                ],
            },
        ],
        DryRun=False,
    )
    expression = jmespath.compile(
        "Reservations[*].Instances[0].{"
        + NAME
        + ":Tags[?Key==`Name`].Value | [0],"
        + IP
        + ":PrivateIpAddress}"
    )
    result = expression.search(response)

    return result


def __get_ip_by_pattern(list, pattern):
    ips = []
    for entry in list:
        if pattern in entry[NAME]:
            ips.append(entry[IP])
    return ips


def get_kafka_broker(region, env):
    list = __get_ec2_ips_and_names(region)
    ip = __get_ip_by_pattern(list, "{}{}".format(env, PATTERN_KAFKA_BROKER))
    return ip


def get_kafka_worker(region, env):
    list = __get_ec2_ips_and_names(region)
    ip = __get_ip_by_pattern(list, "{}{}".format(env, PATTERN_KAFKA_WORKER))
    return ip


def get_kafka_bootstrap(ips):
    list = []
    for ip in ips:
        list.append("{}:{}".format(ip, KAFKA_BOOTSTRAP_PORT))
    return ",".join(list)


def get_parser():
    """get the parsers dict"""
    parsers = {"super": argparse.ArgumentParser(description="Ec2 utility collection")}

    parsers["super"].add_argument(
        "-r",
        "--region",
        default=DEFAULT_REGION,
        help="pass a region or it will be used the default one:" + DEFAULT_REGION,
    )

    parsers["super"].add_argument(
        "-e", "--env", default=None, required=True, help="environment"
    )

    subparsers = parsers["super"].add_subparsers(help="help")

    action = "get-kafka-broker"
    parsers[action] = subparsers.add_parser(action, help="get ip of a Kafka broker")
    parsers[action].set_defaults(action=action)

    action = "get-kafka-worker"
    parsers[action] = subparsers.add_parser(action, help="get ip of a Kafka worker")
    parsers[action].set_defaults(action=action)

    action = "get-kafka-bootstrap"
    parsers[action] = subparsers.add_parser(action, help="get all Kafka brokers")
    parsers[action].set_defaults(action=action)

    return parsers


def main():
    parsers = get_parser()
    args = parsers["super"].parse_args()

    region = args.region
    env = args.env

    if "action" in vars(args):
        if args.action == "get-kafka-broker":
            print(get_kafka_broker(region, env))
            return
        if args.action == "get-kafka-worker":
            print(get_kafka_worker(region, env))
            return
        if args.action == "get-kafka-bootstrap":
            ips = get_kafka_broker(region, env)
            print(get_kafka_bootstrap(ips))
            return
    else:
        parsers["super"].print_help()


if __name__ == "__main__":
    main()
