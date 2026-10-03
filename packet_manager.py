""""""
from command_manager import CommandManager

class PacketManager:
    """
    Менеджер команд, проверяет входящий пакет и во
    """
    COMMANDS = frozenset([
        'start',
        'shutdown',
        'reboot',
        'screenshot',
        'minimize'
        ])
    PACK_SCHEMA = {
        "version": int,
        "tg_id": str,
        "command": str,
        "args": dict
    }   
    
    def checker(self, pack: dict) -> str:
            """_summary_
    
            Args:
                pack (dict): _description_
    
            Returns:
                str: _description_
            """
            self._validate_pack(pack)
            response = self._check_command(pack)
            return response
    #----------- проверка пакета -----------
    def _check_extra_keys(self, pack: dict):
        self._validate_packet_type(pack)
        for key in pack:
            if not key in self.PACK_SCHEMA:
                raise TypeError(f'Ключ {key} лишний!')
    
    def _check_pack_structure(self, pack: dict):
        self._validate_packet_type(pack)
        for key, expected_type in self.PACK_SCHEMA.items():
            if key not in pack:
                raise TypeError(f'Неправильный формат пакета! Отсуствует ключ: {key}')
            elif not isinstance(pack[key], expected_type):
                raise TypeError(f'Ключ {key} имеет недопустимый тип {type(pack[key])}. Нужен {expected_type}')
            
    def _check_pack_command(self, command: str):
        if not isinstance(command, str):
            raise TypeError('command должен быть строкой!')
        if not command in self.COMMANDS:
            raise KeyError(f'Команда {command} не найдена.')
        
    @staticmethod
    def _validate_packet_type(pack):
        if not (isinstance(pack, dict)):
            raise TypeError(f'pack должен быть словарём!')
        
    def _validate_pack(self, pack: dict):
        """
        Проверяет пакет на следующие пункты:
        1) Наличие всех ключей
        2) Совпадение типов содержимого по ключам
        3) Допустимость команд
        4) Наличие лишних ключей
        Args:
            pack (dict): Пакет на проверку
        """
        self._validate_packet_type(pack)
        self._check_pack_structure(pack)
        self._check_extra_keys(pack)
        self._check_pack_command(pack['command'])
    
    #----------- проверка команд -----------
    def _check_command(self, pack):
        CommandManager(pack.command, pack.args)    
    