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

var form_register = document.querySelector ('#wrapper_reg_Form_1');
var form_vxod = document.querySelector ('#wrapper_reg_Form_2');
var btn_to_vhod =document.querySelector ('.btn_to_vhod');
var btn_to_reg =document.querySelector ('.btn_to_reg');

btn_to_vhod.onclick = function () {
	form_register.className = 'wrapper_reg_Form_opacity';
	form_vxod.className = '';
}
btn_to_reg.onclick = function () {
	form_vxod.className = 'wrapper_reg_Form_opacity';
	form_register.className = '';
}

var header_btn_vxod = document.querySelector('#header_btn_vxod');
var header_btn_register = document.querySelector('#header_btn_register');

header_btn_vxod.onclick = function () {
	form_register.className = 'wrapper_reg_Form_opacity';
	form_vxod.className = '';
}
header_btn_register.onclick = function () {
	form_vxod.className = 'wrapper_reg_Form_opacity';
	form_register.className = '';
}

var zaregister = document.querySelector('.input_submit');

zaregister.onclick = function () {
	alert('Вроде как все нормально');
}









