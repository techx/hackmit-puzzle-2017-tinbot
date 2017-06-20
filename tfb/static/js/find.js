$(document).ready(function() {
	if (!localStorage.currentBot) {
		nextBot();
	}
	else {
		setBot(localStorage.currentBot);
	}

	$('.cb').click(function() {
		nextBot();
	});
});

function nextBot() {
	$.get('/api/' + username + '/bot/next', function(resp) {
		setBot(resp);
		localStorage.currentBot = resp;
	});
}

function setBot(jwt) {
	var bot = jwt_decode(jwt);
	$('.profile-name').text(bot.name);
	$('.profile-title').text(bot.profession);
	console.log("Current bot prefers a", bot.preference.label);
}

function checkMatch() {
	$.post('/api/' + username + '/bot/match', data={
		'user_token': localStorage.currentPrediction,
		'bot_token': localStorage.currentBot
	}, function(resp) {
		console.log(resp);
	});
}