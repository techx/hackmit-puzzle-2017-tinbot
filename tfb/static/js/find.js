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

	$('.chb').click(function() {
		checkMatch();
	});

	$('.next-bot').click(function() {
		nextBot();
	})
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
	// No profile picture => no bot likes you.
	if (!localStorage.predictionToken) {
		showMatchMessage("It's not a match.", "The bot can't see you.");
		return;
	}

	$.post('/api/' + username + '/bot/match', data = {
		'user_token': localStorage.predictionToken,
		'bot_token': localStorage.currentBot
	}, function(resp) {
		resp = $.parseJSON(resp);
		console.log(resp);
		if (!resp.match) {
			showMatchMessage("It's not a match.", "The bot doesn't like you back.");
		}
		else {
			showMatchMessage("It's a match!", resp.answer);
		}
	});
}

function showMatchMessage(header, message) {
	$('.modal-header').text(header);
	$('.modal-message').text(message);
	$('.ui.modal').modal({
		blurring: true
	}).modal('show');
}