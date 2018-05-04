# coding=utf-8
import json
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S %p"
)


def transform(list_data):
    """
    将data字段转换成要插入的sql语句
    :return:
    """

    value_list = []

    for data in list_data:

        fields = [
            "id",
            "createdBy",
            "createdOn",
            "lastModifiedBy",
            "lastModifiedOn",
            "createdByName",
            "lastModifiedByName",
            "parentId",
            "projectId",
            "projectName",
            "objectType",
            "type",
            "name",
            "displayName",
            "owner",
            "ownerName",
            "status",
            "deleted",
            "lockedBy",
            "lockedByName",
            "lockedOn",
            "extend",
            "folderId",
            "dataVersion",
            "deployStatus",
            "commitStatus",
            "currentVersion",
            "content",
            "enableScheduler",
            "parentFlowIds",
            "parameters",
            "startEffectedDate",
            "endEffectedDate",
            "suspend",
            "dryRun",
            "cronExpression",
            "dependentedType",
            "dependentedNodes",
            "taskRerunTime",
            "taskRerunInterval",
            "manualTrigger",
            "parentFlows"
        ]

        value = []
        for field in fields:
            if type(data.get(field)) is list:
                value.append(json.dumps(data.get(field), ensure_ascii=False))
            else:
                value.append(data.get(field))
        value.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        value_list.append(value)

    return value_list


if __name__ == "__main__":
    data_list = json.load(open("data_list.txt", encoding="utf-8"))
    res = transform(data_list)
    json.dump(res, open("value_list.txt", "w", encoding="utf-8"), ensure_ascii=False)
