def detection_to_dict(detection):
    return {
        "time": detection.time.isoformat(),  # 转换为 ISO 8601 字符串
        "content": detection.content,
        "picture_url": detection.picture_url,
        "result": detection.result,
    }