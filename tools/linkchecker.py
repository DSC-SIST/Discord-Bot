from pysafebrowsing import SafeBrowsing
import os
import validators
async def checklink(ctx):
    url_checker = SafeBrowsing(os.getenv('GOOGLE_SAFE_BROWSING_API_KEY'))
    link=ctx.message.content.split(" ")[1].strip()
    valid=validators.url(link)
    if not valid:
        ctx.send("Not a url. Check and try again!")
    try:
        response = url_checker.lookup_urls([link])
        if response[link]["malicious"] == False:
            await ctx.send(link + " **is not malicious**")
            return
        elif response[link]["malicious"] == True:
            await ctx.send(link + " **is malicious**")
            return
        else:
            await ctx.send("Awww snap! Something's went wrong.")
    except:
        await ctx.send("There was no link in your command\nExample command: ``check <pastethelinkhere>``")