from discord.ext import commands
from datetime import datetime
from utils.database_utils import add_homework

class HomeworkCommands(commands.Cog):
    """Klass för läxkommandon."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="läxa")
    async def läxa(self, ctx, assignment: str, due_date: str):
        """ Kommando för att lägga till en ny läxa """
        try:
            # Validera datumformat
            datetime.strptime(due_date, '%Y-%m-%d')
            add_homework(assignment, due_date)
            await ctx.send(f"Ny Läxa tillagd: {assignment}, förfallodatum: {due_date}")
        except ValueError:
            await ctx.send("Felaktigt datumformat. Använd YYYY-MM-DD.")

def setup(bot):
    bot.add_cog(HomeworkCommands(bot))

