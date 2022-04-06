package INFLEARN.STEP01

import java.util.Scanner

fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str : String = kb.next()
    println(solution(str))
}

private fun solution(str: String): String {
    var answer = ""

    str.forEach {
        // 문자열에 대한 대문자 소문자 검사 방법
        if(Character.isLowerCase(it)){
            answer += Character.toUpperCase(it)
        }else{
            answer += Character.toLowerCase(it)
        }
    }

    return answer
}
