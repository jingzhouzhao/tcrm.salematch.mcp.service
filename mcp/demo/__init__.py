import httpx
from mcp.server import FastMCP

mcp = FastMCP('web_search', port=19000)

@mcp.tool()
async def web_search(query: str) -> str:
    """
    执行网络搜索并返回结果

    Args:
        query: 搜索查询字符串

    Returns:
        搜索结果字符串
    """
    try:
        # 这里应该是实际的网络搜索逻辑
        # 现在只是简单示例
        return f"{query} 的搜索结果: 天氣晴朗"
    except Exception as e:
        return f"搜索出错: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport='sse')
