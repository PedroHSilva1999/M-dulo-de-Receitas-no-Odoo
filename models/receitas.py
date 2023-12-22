from odoo import models, fields, api

class Receita(models.Model):
    _name = 'meu_modulo_receita'
    _description = 'Modelo para controle de receitas'

    nome = fields.Char(string='Nome da Receita', required=True)
    valor = fields.Float(string='Valor da Receita')
    ingredientes = fields.Many2many('meu_modulo.ingrediente', string='Ingredientes')
    quantidade_ingredientes = fields.Integer(string='Quantidade de Ingredientes', compute='_compute_quantidade_ingredientes', store=True)

    @api.depends('ingredientes')
    def _compute_quantidade_ingredientes(self):
        for receita in self:
            receita.quantidade_ingredientes = len(receita.ingredientes)

class Ingrediente(models.Model):
    _name = 'meu_modulo.ingrediente'
    _description = 'Modelo para ingredientes'

    name = fields.Char(string='Nome do Ingrediente', required=True)