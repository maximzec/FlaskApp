var start_invest_slader_1 = document.querySelector ('#start_invest_slader_1');
var start_invest_slader_2 = document.querySelector ('#start_invest_slader_2');

start_invest_slader_1.onclick = function () {
	start_invest_slader_1.className = 'start_invest_slader';
	start_invest_slader_2.className = '';
}
start_invest_slader_2.onclick = function () {
	start_invest_slader_2.className = 'start_invest_slader';
	start_invest_slader_1.className = '';
}










