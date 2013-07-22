mkdir ~/linuxtimeline_test
mkdir ~/linuxtimeline_test/alpha
mkdir ~/linuxtimeline_test/bravo
mkdir ~/linuxtimeline_test/charlie
sleep 5
mkdir ~/linuxtimeline_test/alpha/delta
sleep 5
mkdir ~/linuxtimeline_test/bravo/echo
sleep 10
mkdir ~/linuxtimeline_test/alpha/delta/fox

echo "number1" > ~/linuxtimeline_test/number1.txt
echo "number2" > ~/linuxtimeline_test/alpha/number2.txt
sleep 1
echo "number3" > ~/linuxtimeline_test/alpha/number3.txt
sleep 3
echo "number4" > ~/linuxtimeline_test/bravo/echo/number4.txt
sleep 5
echo "number5" > ~/linuxtimeline_test/alpha/delta/fox/number5.txt
sleep 5
echo "number6" > ~/linuxtimeline_test/alpha/delta/fox/number6.txt