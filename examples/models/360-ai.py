import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from browser_use import Agent

# 加载环境变量
load_dotenv()

# 从环境变量获取360 API Key
ai360_api_key = os.getenv('AI_360_API_KEY', '')
if not ai360_api_key:
    raise ValueError('AI360_API_KEY is not set in .env file')

async def run_360_search():
    agent = Agent(
        task='1.访问：https://ucng2j2hu7zx.feishu.cn/drive/home/; 2.新建一个空白表格，将本次调试过程填写到表格中；3.保存文档',
        llm=ChatOpenAI(
            base_url='https://api.360.cn/v1/',  # 修正API基础地址
            model='deepseek-r1',
            api_key=SecretStr(ai360_api_key),
            default_headers={
                "Authorization": f"Bearer {ai360_api_key}"
            }
        ),
        use_vision=False,
        max_failures=2,
        max_actions_per_step=1,
    )

    await agent.run()

if __name__ == '__main__':
    asyncio.run(run_360_search()) 