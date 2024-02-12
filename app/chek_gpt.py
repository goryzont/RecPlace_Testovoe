import g4f
import asyncio


async def ask_gpt(promt: str) -> str:
    response = await g4f.ChatCompletion.create_async(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": promt}],
    )  # Alternative model setting

    return response

_providers = [
    g4f.Provider.AItianhu,
    g4f.Provider.AItianhuSpace,
    g4f.Provider.AiAsk,
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.ChatForAi,
    g4f.Provider.ChatgptAi,
    g4f.Provider.ChatgptX,
    g4f.Provider.FakeGpt,
    g4f.Provider.FreeGpt,
    g4f.Provider.GPTalk,
    g4f.Provider.GptForLove,
    g4f.Provider.GptGo,
    g4f.Provider.Hashnode,
    g4f.Provider.MyShell,
    g4f.Provider.NoowAi,
    g4f.Provider.OpenaiChat,
    g4f.Provider.Theb,
    g4f.Provider.Vercel,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
    g4f.Provider.Bing,
    g4f.Provider.GeekGpt,
    g4f.Provider.GptChatly,
    g4f.Provider.Liaobots,
    g4f.Provider.Phind,
    g4f.Provider.Raycast,
]


async def run_provider( provider: g4f.Provider.BaseProvider):
    try:
        response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hey"}],
            provider=provider,
        )

        print(f"{provider.__name__}:", response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all():
    calls = [
        run_provider(provider) for provider in _providers
    ]
    await asyncio.gather(*calls)

asyncio.run(run_all())

#print(run_provider(g4f.Provider.ChatgptAi, "Кто сейчас президент Америки"))