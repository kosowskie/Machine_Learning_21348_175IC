## Otwieranie i zamykanie pliku w Pythonie

Odbywa się to poprzez wywołanie funkcji wbudowanej open (). open () ma jeden wymagany argument, którym jest ścieżka do pliku.

## try-finally / with statements

Manipulując plikiem, można skorzystać z dwóch sposobów, aby upewnić się, że plik zostanie poprawnie zamknięty. Pierwszym sposobem zamknięcia pliku jest użycie bloku try-last. Drugim sposobem zamknięcia pliku jest użycie instrukcji with.

## Text File Types

TextIOWrapper - domyślny obiekt zwracany przez open ().
Buffered - do odczytywania i zapisywania plików binarnych używany jest obiekt pliku binarnego.

## Raw File Types

Raw File - zwykle używany jako kod niskiego poziomu dla strumieni binarnych i tekstowych.

## Reading and Writing Opened Files

.read(size=-1) - odczytuje z pliku na podstawie liczby bajtów. Jeśli nie zostanie przekazany żaden argument lub None lub wartość -1, odczytywany jest cały plik.
.readline(size=-1) - Odczytuje rozmiar liczby znaków z wiersza. Jeśli nie zostanie przekazany żaden argument lub None lub -1, to odczytywana jest cała linia.
.readlines() - Czyta pozostałe wiersze z obiektu pliku i zwraca je jako listę.

## Iterating Over Each Line in the File

Typową rzeczą do zrobienia podczas czytania pliku jest iteracja po każdej linii. Możemy to wykonać poprzez .readline lub .readlines.

## Working With Bytes

Czasami może zajść potrzeba pracy z plikami przy użyciu stringów. Odbywa się to poprzez dodanie znaku „b” do argumentu trybu.

## Appending to a File

Python umozliwia dołączanie do pliku lub rozpoczynanie pisania na końcu już zapełnionego pliku. Można to łatwo zrobić, używając znaku „a” jako argumentu trybu.

## Working With Two Files at the Same Time

Python umożliwia operację na dwóch plikach jednoczesnie. Zapis jak i odczyt asynchornicznie.

## Creating Your Own Context Manager

Python umożliwia kontrolę nad obiektem pliku poprzez umieszczenie go w custom klasie. W przypadku użycia, nie można już używać instrukcji with, chyba że doda się kilka magicznych metod: __enter__ i __exit__. Dodając je tworzy się context manager.
