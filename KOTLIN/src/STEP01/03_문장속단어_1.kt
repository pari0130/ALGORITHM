package STEP01

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

private fun solution(str: String): String {
    var answer = ""
    var m = Integer.MIN_VALUE
    val s : List<String> = str.split(' ')

    s.forEach{
        // println(it)
        val len = it.length
        if(len > m){
            m = len
            answer = it
        }
    }

    return answer
}
