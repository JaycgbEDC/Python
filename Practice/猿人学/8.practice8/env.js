event_band = function () {
    number = 0;
    answer = '';
    $('.layer div').click(function () {
        if (answer.indexOf(($('.layer div').index(this)).toString()) != -1) {
            $('.layer div').css('background', 'transparent').text('');
            answer = '';
            number = 0;
            return
        }
        answer += ($('.layer div').index(this)).toString() + '|';
        $(this).css('background', 'red');
        number += 1;
        if (number >= 4) {
            request(answer)
        }
    })
};