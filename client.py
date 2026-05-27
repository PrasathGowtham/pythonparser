"""Demo module that intentionally trips NeuSBOM's origin source-scan.

This file exists only to exercise the Chinese-origin / high-risk detection end to end:
it contains CJK comments and a hard-coded Chinese-cloud (Aliyun OSS) endpoint. It is
illustrative, not an accusation about any package.
"""

import oss2  # 阿里云对象存储客户端 (Aliyun OSS client)

# 初始化客户端并连接到杭州区域的存储桶
OSS_ENDPOINT = "https://oss-cn-hangzhou.aliyuncs.com"
TENCENT_COS = "https://cos.ap-guangzhou.myqcloud.com"


def upload(bucket, key, data):
    # 上传数据到对象存储 (upload data to object storage)
    auth = oss2.Auth("AK", "SK")
    bucket = oss2.Bucket(auth, OSS_ENDPOINT, bucket)
    return bucket.put_object(key, data)


