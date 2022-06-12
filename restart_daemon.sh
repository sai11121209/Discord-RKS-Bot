#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl restart discord-bot-rks.service
sudo systemctl status discord-bot-rks.service