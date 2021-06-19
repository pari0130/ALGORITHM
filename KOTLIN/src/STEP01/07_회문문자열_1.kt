package STEP01

import java.lang.StringBuilder
import java.util.Scanner

// 회문 문자열 비교, 문자열을 뒤집어도 같은지 체크 함
// teet : yes, test : no
fun main() {
    val kb: Scanner = Scanner(System.`in`)
    val str = kb.next()
    println(solution(str))
}

private fun solution(str: String): String {
    var answer = "YES"
    val len = str.length

    // get() 으로 가저오는 문자도 0 번 인덱스 부터 접근함
    for(i in 0..len/2){
        if(str.toUpperCase().get(i) != str.toUpperCase().get(len-i-1)){
            answer = "NO"
            break
        }
    }

    return answer
}