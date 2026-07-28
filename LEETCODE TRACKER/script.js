function stats(){
    user=document.getElementById("username")
    name=user.value
    fetch(`https://leetcode-stats.tashif.codes/${name}`)
        .then(response=>response.json())
        .then(
            data=>{document.getElementById("easy").innerText=data.easySolved
                   document.getElementById("medium").innerText=data.mediumSolved
                   document.getElementById("hard").innerText=data.hardSolved
                   document.getElementById("rank").innerText=data.ranking
        })
}