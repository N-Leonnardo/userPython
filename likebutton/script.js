var likes = document.querySelector("#likes")
count = 0

function liked(element){
    count++
    likes.innerText = "Likes:" +count
}