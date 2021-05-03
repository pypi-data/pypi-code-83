import os
import math
import asyncio
import datetime

import discord 
from discord.ext import tasks
from .utils import snapshot_proposal_url
from .proposal_monitor import ProposalMonitor 
from .constants import CHECK_FREQUENCY, SNAPSHOT_PROPOSAL_URL


class ProposalMonitorDiscord:
    def __init__(self, discord_client, *args, **kwargs):
        self.discord_client = discord_client
        self.channel_name = kwargs.get('channel_name', os.getenv('DISCORD_OUTPUT_CHANNEL'))
        self.persistent_location = kwargs.get('persistent_location', os.getenv('PERSISTENT_LOCATION'))
        self.proposal_monitor = ProposalMonitor(**kwargs)
        # restore state if provided.
        if self.persistent_location:
            self.proposal_monitor.load(self.persistent_location)
        # "main"
        self.pm_task = self.discord_client.loop.create_task(self.proposal_watch())

    def get_output_channel(self):
        """Get the discord output channel based on the init param 'channel_name' and set self.output_channel."""
        for channel in self.discord_client.get_all_channels():
            if channel.name == self.channel_name:
                self.output_channel = channel

    def _embed_field_value_limit(self, value):
        """Respect the character limt of discord.Embed field length limits.
        Returns a str less than 1024
        """
        if len(value) > 1024:
            return value[:1020] + "..."
        return value
    
    def _time_left(self, proposal):
        """Return a human readable message for time left in hours or minutes."""
        hours_til_expire = math.floor(proposal.time_until_expire() / 3600) 
        minuites_til_expire = math.floor(proposal.time_until_expire() / 60)
        if hours_til_expire > 0:
            time_left = f"< {hours_til_expire} hours" 
        else:
            time_left = f"< {minuites_til_expire} minutes"
        return time_left

    def proposals_to_discord_message(self, proposals):
        """Return a list of 2-tuples containing, respectively, a string and a discord.Embed message for proposals."""
        messages = []
        for proposal in proposals:
            title = self._embed_field_value_limit(proposal.name)
            body = self._embed_field_value_limit(proposal.body)
            url = snapshot_proposal_url(proposal)
            color = self.proposal_monitor.get_proposal_color(proposal)
            end_date = datetime.datetime.fromtimestamp(proposal.end_time).strftime('%B %d, %Y %H:%M UTC')
            time_left = self._time_left(proposal)
            
            embed = discord.Embed(title=title, url=url, color=color)
            embed.add_field(name="Space", value=proposal.space, inline=False)
            embed.add_field(name="Description", value=body, inline=False)
            if proposal.is_active():
                msg = "**Active**"
                embed.add_field(name="Voting Ends", value=end_date, inline=True)
                embed.add_field(name="Voting Timeleft", value=time_left, inline=True)
            else:
                msg = "**Recently Closed**"
                embed.add_field(name="Voting Timeleft", value="Closed", inline=False)
            
            messages.append((msg, embed))
        return messages

    async def proposal_watch(self, **kwargs):
        """An async task to fetch, save, and notify about active proposals from ProposalMonitor.
        Inteneded to be used as a parameter in discord.Client.loop.create_task.
        """
        await self.discord_client.wait_until_ready()
        self.get_output_channel()
        while not self.discord_client.is_closed():
            # fetch
            proposals_to_alert = self.proposal_monitor.get_proposals_to_alert()
            # save
            if self.persistent_location: 
                self.proposal_monitor.dump(self.persistent_location)
            # notify
            messages = self.proposals_to_discord_message(proposals_to_alert)
            for message in messages:
                msg, embed = message
                await self.output_channel.send(msg, embed=embed)
            # sleep
            await asyncio.sleep(CHECK_FREQUENCY)

"""
    TODO: A health check to be used container management libraries. 
    async def healthy(self):
        await self.discord_client.wait_until_ready()
        return self.pm_task.is_running()
"""