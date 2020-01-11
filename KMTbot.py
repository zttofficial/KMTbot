const TelegramBot = require('node-telegram-bot-api');
const request = require('request');

const token = 'Your Token';
const bot = new TelegramBot(token, {
  polling: true
});

bot.onText(/\/officer/, function KMTofficer(msg) {
  bot.sendSticker(msg.chat.id, 'CAADBQADIwAD4RTDG2se4dhpZE0DFgQ');
});


bot.sendSticker(id, sticker[0]).then(message => {
            let cid = message.chat.id;
            let mid = message.message_id;
            if (data.autodelete[cid] && data.lastid[cid]) {
                bot.deleteMessage(cid, data.lastid[cid]);
            }
            data.lastid[cid] = mid;
            saveData();
        }))

 
if (e.parameter.runAutoTask){
   AutoTask();
   return HtmlService.createHtmlOutput(e.parameter.runAutoTask);
}

function AutoSendSticker() {
  var payload = {
    "method": "sendPhoto",
    "chat_id": 539065210,
    "sticker": "CAADBQADIwAD4RTDG2se4dhpZE0DFgQ"
  };
 
  postTelegram(payload);
}
 
 
function AutoTask() {
  AutoSendSticker();
}
