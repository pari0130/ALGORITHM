package INFLEARN.STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 중복된 문자열 제거 출력
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}

private fun solution(str: String): String {
    var answer = ""
    //
    for(i in 1..str.length){
        if(str.indexOf(str.get(i)) == i) answer += str.get(i)
    }

    return answer
}