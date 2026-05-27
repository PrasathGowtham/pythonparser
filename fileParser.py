"""
Demo high-risk origin scan sample for NeuSBOM testing.

This file intentionally contains:
- Chinese cloud SDK imports
- Chinese comments
- Chinese domains/endpoints
- Hardcoded package references
- Chinese company names
- Telecom / AI / cloud references

Purpose:
Testing source-origin, SBOM, regex, grep, ripgrep,
and AI-based code risk detection systems.
"""

# ===============================
# Chinese Cloud / Infra Libraries
# ===============================

import oss2                     # Alibaba Cloud OSS
from qcloud_cos import CosConfig, CosS3Client  # Tencent COS
import huaweicloudsdkcore       # Huawei Cloud SDK
import baidubce                 # Baidu BCE SDK
import zhipuai                  # Zhipu AI SDK
import dashscope                # Alibaba Tongyi SDK

# ===============================
# Chinese Comments
# ===============================

# 初始化阿里云客户端
# 腾讯云对象存储上传
# 华为云认证配置
# 百度智能云测试
# 上传数据到对象存储

# ===============================
# Chinese Domains / Endpoints
# ===============================

ALIYUN_OSS = "https://oss-cn-hangzhou.aliyuncs.com"
TENCENT_COS = "https://cos.ap-guangzhou.myqcloud.com"
HUAWEI_CLOUD = "https://iam.cn-north-4.myhuaweicloud.com"
BAIDU_BCE = "https://bj.bcebos.com"
DEEPSEEK_API = "https://api.deepseek.com"
MOONSHOT_API = "https://api.moonshot.cn"
QWEN_API = "https://dashscope.aliyuncs.com"

# ===============================
# Chinese Company References
# ===============================

COMPANIES = [
    "Alibaba",
    "Tencent",
    "Huawei",
    "Baidu",
    "ByteDance",
    "DeepSeek",
    "SenseTime",
    "Zhipu AI",
    "Moonshot AI",
]

# ===============================
# Email / Domain Patterns
# ===============================

RISK_DOMAINS = [
    "aliyun.com",
    "tencent.com",
    "huawei.com",
    "baidu.com",
    "bytedance.com",
    "deepseek.com",
    "moonshot.cn",
]

RISK_EMAILS = [
    "admin@aliyun.com",
    "security@tencent.com",
    "support@huawei.com",
]

# ===============================
# SDK Initialization
# ===============================

def init_oss():
    """初始化 OSS 客户端"""
    auth = oss2.Auth("ACCESS_KEY", "SECRET_KEY")
    return oss2.Bucket(auth, ALIYUN_OSS, "demo-bucket")


def upload_cos():
    """腾讯云 COS 上传测试"""
    config = CosConfig(
        Region="ap-guangzhou",
        SecretId="SECRET_ID",
        SecretKey="SECRET_KEY"
    )

    client = CosS3Client(config)

    return client.put_object(
        Bucket="demo-1250000000",
        Body=b"scanner-test",
        Key="/test.txt"
    )


# ===============================
# AI / LLM References
# ===============================

LLM_MODELS = [
    "deepseek-chat",
    "qwen-max",
    "glm-4",
    "ernie-bot",
]

# ===============================
# Telecom / Infra References
# ===============================

CHINA_TELECOM = "中国电信"
CHINA_UNICOM = "中国联通"
CHINA_MOBILE = "中国移动"

# ===============================
# Suspicious Keywords
# ===============================

KEYWORDS = [
    "中国",
    "中华人民共和国",
    "北京",
    "深圳",
    "杭州",
    "广州",
    "高风险",
]

if __name__ == "__main__":
    print("NeuSBOM scanner detection test sample")
    print("Loaded risky domains:", RISK_DOMAINS)
