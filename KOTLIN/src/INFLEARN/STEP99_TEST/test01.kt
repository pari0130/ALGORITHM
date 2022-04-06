package INFLEARN.STEP99_TEST

/*
* <div 클래스="brinza-task-description">
<p>길이가 N인 문자열 S가 주어지면 S의 모든 물음표를 소문자('a'-'z')로 대체하여 얻을 수 있는 모든 회문을 반환하는 함수 <tt style="white-space:pre-fre-tt]를 작성한다. 회문을 얻을 수 없는 경우 함수는 문자열 "NO"를 반환해야 한다.</p>
<p>회문은 앞뒤로 같은 것을 읽는 문자열이다. 회문에는 "카약", "레이더", "엄마" 등이 있다.</p>
<p>예:
<p>1. 주어진 S = "?ab?"?a", 함수는 "aabbaa"를 반환해야 한다.</p>
<p>2. 주어진 S = "bab?"?a", 함수는 "NO"를 반환해야 한다.</p>
<p>3. S = "?a??"가 주어지면 함수는 "signed"를 반환할 수 있습니다. 또한 다른 가능한 답변 중 "zaz"를 반환할 수도 있습니다.</p>
<p>다음과 같이 가정하다.
<블록 인용><울 스타일=>10px;10px;"0px;">N은 [<span class="number">1</span> 범위 내의 정수이다.<span class="숫자">1,000</span];</li>
<li> 문자열 S는 소문자('a' - 'z') 또는 '?)로만 구성된다.</li>
</ul>
</블록인용><p>당신의 해결책으로, 정확성에 집중하세요. 솔루션의 성과는 평가의 초점이 아닙니다.</p>
</div>
* */
fun main(){

    val t1 = "?ab??a"
    val t2 = "bab??a"
    val t3 = "?a?"

    println(solution(t1))
    println(solution(t2))
    println(solution(t3))
}

private fun solution(s: String) : String{

    val fail = "NO"
    val convertStr = "z".single()
    val replaceTarget = "?".single()
    val length = s.length
    val list: MutableList<Char>

    if(s.isEmpty() || length == 1){
        return fail
    } else {
        list = s.toMutableList()
    }

    for(i in 0..length/2) {
        run {
            if(length%2 == 0) {
                if(list[i] == replaceTarget) {
                    list[i] = list[length-i-1]
                }
                if(list[length-i-1] == replaceTarget){
                    list[length-i-1] = list[i]
                }
            } else {
                if(list[i] == list[length-1]) {
                    list[i] = convertStr
                    list[length-1] = convertStr
                }
            }
        }

        if (list[i] != list[length-i-1]) {
            return fail
        }
    }

    return list.joinToString("")
}