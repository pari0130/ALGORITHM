package INFLEARN.STEP01

import java.util.Scanner

// 문장 속에서 가장 길이가 긴 단어를 찾기
/*
* it is s aStrwrS Strign aasdwe sdSt asdas Strewknrq
* Strewknrq
* */
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str : String = kb.nextLine()
    println(solution(str))
}

private fun solution(paramStr: String): String {
    var str = paramStr
    var answer = ""
    var m : Int = Integer.MIN_VALUE
    var pos : Int = 0

    while (str.indexOf(' ') != -1){
        pos = str.indexOf(' ')
        val tmp = str.substring(0, pos)
        val len : Int = tmp.length
        if(len > m){
            m = len
            answer = tmp
        }
        str = str.substring(pos+1)
    }

    if(str.length > m) answer = str

    return answer
}
