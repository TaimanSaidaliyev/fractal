let input_message = $('#input-message')
let message_body = $('.msg_card_body')
let send_message_form = $('#send-message-form')
const USER_ID = $('#logged-in-user').val()

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'https') {
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint+'ws/socket-server')

socket.onopen = async function(e){
    console.log('open', e)
    send_message_form.on('submit', function (e){
        e.preventDefault()
        let message = input_message.val()
        let send_to = get_active_other_user_id()
        let thread_id = get_active_thread_id()

        let data = {
            'message': message,
            'sent_by': USER_ID,
            'send_to': send_to,
            'thread_id': thread_id
        }
        data = JSON.stringify(data)
        socket.send(data)
        $(this)[0].reset()
    })

}

socket.onmessage = async function(e){
    console.log('message', e)
    let data = JSON.parse(e.data)
    let message = data['message']
    let sent_by_id = data['sent_by']
    let thread_id = data['thread_id']
    let timestamp = data['timestamp']
    newMessage(message, sent_by_id, thread_id, timestamp)
    console.log('onmessage',e)
}

socket.onerror = async function(e){
    console.log('error', e)
}

socket.onclose = async function(e){
    console.log('close', e)
}


function newMessage(message, sent_by_id, thread_id, timestamp) {
	if ($.trim(message) === '') {
		return false;
	}
	let message_element;
	let chat_id = thread_id
	if(sent_by_id == USER_ID){
	    message_element = `
			<div class="d-flex justify-content-end mb-10">
                <!--begin::Wrapper-->
                <div class="d-flex flex-column align-items-end">
                    <!--begin::User-->
                    <div class="d-flex align-items-center mb-2">
                        <!--begin::Details-->
                        <div class="me-3">
                            <span class="text-muted fs-7 mb-1">${timestamp}</span>
                        </div>
                        <!--end::Details-->
                    </div>
                    <!--end::User-->
                    <!--begin::Text-->
                    <div class="p-5 rounded bg-light-primary text-dark fw-semibold mw-lg-400px text-end" data-kt-element="message-text">${message}</div>
                    <!--end::Text-->
                </div>
                <!--end::Wrapper-->
            </div>
	    `
    }
	else{
	    message_element = `
        <div class="d-flex justify-content-start mb-10">
            <div class="d-flex flex-column align-items-start">
                <div class="d-flex align-items-center mb-2">
                    <div class="symbol symbol-35px symbol-circle">
                        <img alt="Pic" src="assets/media/avatars/300-25.jpg">
                    </div>
                    <div class="ms-3">
                        <a href="#" class="fs-5 fw-bolder text-gray-900 text-hover-primary me-1">${sent_by_id}</a>
                        <span class="text-muted fs-7 mb-1">${timestamp}</span>
                    </div>
                </div>
                <div class="p-5 rounded bg-light-info text-dark fw-bold mw-lg-400px text-start" data-kt-element="message-text">${message}</div>
            </div>
        </div>
        `
    }

    let message_body = $('.messages-wrapper[chat-id="' + chat_id + '"] .msg_card_body')
	message_body.append($(message_element))
    message_body.animate({
        scrollTop: $(document).height()
    }, 100);
	input_message.val(null);
}

$('.contact-li').on('click', function (){
    $('.contacts .active').removeClass('active')
    $(this).addClass('active')
    // message wrappers
    let chat_id = $(this).attr('chat-id')
    $('.messages-wrapper.is_active').removeClass('is_active')
    $('.messages-wrapper[chat-id="' + chat_id +'"]').addClass('is_active')
    console.log('do it')
})

function get_active_other_user_id(){
    let other_user_id = $('.messages-wrapper.is_active').attr('other-user-id')
    other_user_id = $.trim(other_user_id)
    return other_user_id
}

function get_active_thread_id(){
    let chat_id = $('.messages-wrapper.is_active').attr('chat-id')
    let thread_id = chat_id
    return thread_id
}