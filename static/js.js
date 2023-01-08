

function CloseModal(){
    document.getElementById('modalcontainer').style.display = 'none';
    document.getElementById('container').style.filter = 'none';

}

function ShowModal(){
    document.getElementById('modalcontainer').style.display = 'flex';
    document.getElementById('container').style.filter = 'blur(15px)';
    document.getElementById('usernameinput').value = '';
    document.getElementById('emailinput').value = '';
    document.getElementById('passwordinput').value = '';

}

function ShowSignup(){
    document.getElementById('emailinputdiv').style.display = 'flex';
    document.getElementById('modalloginbtn').style.borderColor = 'white';
    document.getElementById('modalsignupbtn').style.borderColor = 'aqua';

}

function ShowLogin(){
    document.getElementById('emailinputdiv').style.display = 'none';
    document.getElementById('emailinput').value = '';
    document.getElementById('modalloginbtn').style.borderColor = 'aqua';
    document.getElementById('modalsignupbtn').style.borderColor = 'white';

}

var ajax_url = "http://127.0.0.1:8000/site_actions/"

function LikeMovie(id,user){
    document.getElementById('progressbar').style.display = 'flex';
    
    $.ajax({
        type : 'POST',
        url : ajax_url,
        data : {
            action : 'like_movie',
            movie_id : id,
        },
        
        success : function(response){
            console.log(response['msg'])
            document.getElementById('progressbar').style.display = 'none';
            if (response['msg'] === 'liked'){
                document.getElementById('likebtn'+id).innerHTML = '&#10084;';
                
            } else if (response['msg'] === 'unliked') {
                document.getElementById('likebtn'+id).innerHTML = '&#9825;';

            } else {
                console.log(response['msg'])
                ShowModal()

            }
            
        }
    })

    
    

}


function Logout(){
    document.getElementById('progressbar').style.display = 'flex'
    console.log('logout...')
    $.ajax({
        type: 'POST',
        url : ajax_url,
        data : {
            action : 'logout',
            
        },
        success : function(response){
            document.getElementById('progressbar').style.display = 'none'
            console.log('logouted')
            if (response['msg'] == 'logged out'){
                var likebtns = document.getElementsByClassName('likebtn');
                for (var i=0; i < likebtns.length; i++){
                    likebtns.item(i).innerHTML = '&#9825';
                }

                try{
                    document.getElementById('logoutdiv').style.display = 'none';
                } catch{

                }
                document.getElementById('logoutdivajax').style.display = 'none';
                document.getElementById('favorite').style.display = 'none';
                document.getElementById('loginbtnajax').style.display = 'flex';

            }
            

        }
    })
}

function SubmitForm(){
    let username = document.getElementById('usernameinput').value;
    let email = document.getElementById('emailinput').value;
    let password = document.getElementById('passwordinput').value;
    document.getElementById('progressbarsignup').style.display = 'flex';
    if (username !== '' && email !== '' && password !== ''){
        $.ajax({
            type : 'POST',
            url : ajax_url,
            data : {
                action : 'signup',
                username : username,
                email : email,
                password : password
            },
            
            success : function(response){
                document.getElementById('progressbarsignup').style.display = 'none';
                CloseModal()
                
            }
        })
    } else if(username !== '' && email == '' && password !== ''){
        $.ajax({
            type : 'POST',
            url : ajax_url,
            data : {
                action : 'login',
                username : username,
                password : password
            },
            
            success : function(response){
                CloseModal()
                document.getElementById('progressbarsignup').style.display = 'none';
                if (response['msg']==='logged in'){
                    try{
                        document.getElementById('loginbtn').style.display = 'none';
                    }catch{
                        
                    }

                    for (var i=0; i < response['liked'].length; i++){
                        console.log(response['liked'][i]['id'])
                        document.getElementById('likebtn'+response['liked'][i]['id']).innerHTML = '&#10084;';
                    }

                    document.getElementById('logoutdivajax').style.display = 'flex';
                    document.getElementById('favorite').style.display = 'flex';
                    document.getElementById('loginbtnajax').style.display = 'none';
                    document.getElementById('usernamelabelajax').innerHTML = response['username'];

                }

            }
        })

    }
    
}


// JS for Animation
function HideProgress(){
    if (document.readyState === 'ready' || document.readyState === 'complete' ){
        console.log('Working....')
        document.getElementById('progressbar').style.display = 'none';
    }
}

function CheckLogin(){
    document.getElementById('progressbar').style.display = 'flex';
    $.ajax({
        type: 'POST',
        url : ajax_url,
        data : {
            action : 'check_login'
        },
        success : function(response){
            document.getElementById('progressbar').style.display = 'none';
            if (response['msg']=== 'true'){
                document.getElementById('logoutdivajax').style.display = 'flex';
                document.getElementById('favorite').style.display = 'flex';
                document.getElementById('usernamelabelajax').innerHTML = response['username'];
            } else if (response['msg']==='false'){
                document.getElementById('loginbtnajax').style.display = 'flex';
                document.getElementById('favorite').style.display = 'none';
            }

        }
    })
}