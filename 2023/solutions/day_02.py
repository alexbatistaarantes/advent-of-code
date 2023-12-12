from re import search, findall

class CubeConundrum:
    
    def get_possible_games(games, cubes):
                
        id_sum = 0

        for game in games.split('\n'):
            id, reveals = CubeConundrum.parse_game_line(game)
            
            for cube, qtd in reveals:
                if qtd > cubes[cube]:
                    break
            else:
                id_sum += id

        return id_sum

    def get_power_from_games(games):
        
        sum_of_power = 0

        for game in games.split('\n'):
            _, reveals = CubeConundrum.parse_game_line(game)

            # max quantity of each cube in this game
            set_of_cubes = {}
            for cube, qtd in reveals:
                if qtd > set_of_cubes.get(cube, 0):
                    set_of_cubes[cube] = qtd

            # power of this game
            power = 1
            for qtd in set_of_cubes.values():
                power *= qtd
            
            sum_of_power += power

        return sum_of_power

    def parse_game_line(game):

        id = int(search(r"^Game (\d*):", game).group(1))

        # reveals = [ ('red', 3), ('blue', 5), ('red', 10) ]
        reveals = []
        for qtd, cube in findall("([0-9]+)\s([a-z]*)[,;]?", game):
            reveals.append( (cube, int(qtd)) )
        
        return id, reveals
    